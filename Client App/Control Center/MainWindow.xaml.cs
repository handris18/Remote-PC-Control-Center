using System.Diagnostics;
using System.IO;
using System.Windows;
using System.Windows.Media;
using Control_Center.Model;
using Control_Center.Model.LoginPopup;


namespace Control_Center
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        private PythonExecuter executer;
        private Server_comm server_comm;
        private string username;

        public MainWindow()
        {
            executer = new PythonExecuter();
            server_comm = new Server_comm();
            string filePath = AppDomain.CurrentDomain.BaseDirectory;
            filePath = filePath.Replace("\\bin\\Debug\\net8.0-windows", "");
            Directory.SetCurrentDirectory(filePath);
            username = File.ReadAllLines("Persistence/UID.txt")[0];
            InitializeComponent();
            if (!File.Exists("Persistence/Registered.txt"))
            {
                connect.IsEnabled = false;
            }
        }

        private async void Register_Click(object sender, RoutedEventArgs e)
        {
            var registerWindow = new RegisterWindow(username);
            if (registerWindow.ShowDialog() == true)
            {
                string in_password = registerWindow.Password;
                if (in_password != "" && username != "")
                {
                    string filePath = AppDomain.CurrentDomain.BaseDirectory;
                    filePath = filePath.Replace("\\bin\\Debug\\net8.0-windows", "");
                    Directory.SetCurrentDirectory(filePath);
                    if (File.Exists("Persistence/Registered.txt") )
                    {
                        MessageBox.Show("Device already registered!");
                        register.IsEnabled = false;
                        return;
                    }

                    var data = new Dictionary<string, string>
                    {
                        { "device_number" , username },
                        { "password" , in_password }
                    };

                    var url = "http://localhost:5000/register";
                                        
                    if (await server_comm.Reg_to_Server(data, url))
                    {
                        File.Create("Persistence/Registered.txt").Close();
                        MessageBox.Show($"Registered as: {username}");
                        register.IsEnabled = false;
                        connect.IsEnabled = true;
                    }
                    else
                    {
                        MessageBox.Show($"Registration failed: error code {server_comm.error_code}");
                    }
                }
            }
            else
            {
                MessageBox.Show("Registration canceled");
            }
        }

        private async void Connect_Click(object sender, RoutedEventArgs e)
        {
            string filePath = AppDomain.CurrentDomain.BaseDirectory;
            filePath = filePath.Replace("\\bin\\Debug\\net8.0-windows", "");
            Directory.SetCurrentDirectory(filePath);
            var loginWindow = new LoginWindow(username);
            if (loginWindow.ShowDialog() == true)
            {
                if (File.Exists("Persistence/Registered.txt"))
                {
                    string in_password = loginWindow.Password;

                    var data = new Dictionary<string, string>
                    {
                        { "device_number" , File.ReadAllLines("Persistence/UID.txt")[0] },
                        { "password" , in_password }
                    };
                    var url = "http://localhost:5000/login";

                    var comm = await server_comm.Login_to_Server(data, url);

                    if (comm.Item1)
                    {
                        MessageBox.Show($"Logged in as: {username}");
                        executer.run_script(data["device_number"], comm.Item2);
                        connect.IsEnabled = false;
                        Connected.Fill = Brushes.Green;
                    }
                    else
                    {
                        MessageBox.Show($"Login failed: error code {server_comm.error_code}");
                    }
                }    
            }
            else
            {
                // Login canceled
                MessageBox.Show("Login canceled");
            }
            
        }

        private void Disconnect_Click(object sender, RoutedEventArgs e)
        {
            executer.kill_script();
            connect.IsEnabled = true;
            Connected.Fill = Brushes.Red;
        }

        private void Exit_Click(object sender, RoutedEventArgs e)
        {
            executer.kill_script();
            Environment.Exit(0);
        }
    }
}