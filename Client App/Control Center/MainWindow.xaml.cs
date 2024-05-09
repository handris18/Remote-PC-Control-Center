using System.Diagnostics;
using System.IO;
using System.Windows;
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

        public MainWindow()
        {
            executer = new PythonExecuter();
            server_comm = new Server_comm();
            InitializeComponent();
        }

        private void Register_Click(object sender, RoutedEventArgs e)
        {
            var loginWindow = new LoginWindow();
            if (loginWindow.ShowDialog() == true)
            {
                string in_username = loginWindow.Username;
                string in_password = loginWindow.Password;
                if (in_password != "" && in_username != "")
                {
                    string filePath = AppDomain.CurrentDomain.BaseDirectory;
                    filePath = filePath.Replace("\\bin\\Debug\\net8.0-windows", "");
                    Directory.SetCurrentDirectory(filePath);
                    if (File.Exists("Persistence/Registered.txt") )
                    {
                        MessageBox.Show("Device already registered!");
                        return;
                    }

                    var data = new
                    {
                        device_number = File.ReadAllText("Persistence/UID.txt"),
                        password = in_password
                    };
                    var url = "localhost:5000/register";
                    server_comm.Send_to_Server(data, url);
                    
                    if (server_comm.success)
                    {
                        File.Create("Persistence/Registered.txt").Close();
                        MessageBox.Show($"Registered as: {in_username}");
                    }
                    else
                    {
                        MessageBox.Show($"Registration failed: error code {server_comm.error_code}");
                    }
                }
            }
            else
            {
                // Login canceled
                MessageBox.Show("Registration canceled");
            }
        }

        private void Unregister_Click(object sender, RoutedEventArgs e)
        { }

        private void Connect_Click(object sender, RoutedEventArgs e)
        {
            string filePath = AppDomain.CurrentDomain.BaseDirectory;
            filePath = filePath.Replace("\\bin\\Debug\\net8.0-windows", "");
            Directory.SetCurrentDirectory(filePath);
            var loginWindow = new LoginWindow();
            if (loginWindow.ShowDialog() == true)
            {
                if (File.Exists("Persistence/Registered.txt"))
                {
                    string in_username = loginWindow.Username;
                    string in_password = loginWindow.Password;

                    var data = new
                    {
                        device_number = File.ReadAllText("Persistence/UID.txt"),
                        password = in_password
                    };
                    var url = "localhost:5000/login";
                    server_comm.Send_to_Server(data, url);

                    if (server_comm.success)
                    {
                        MessageBox.Show($"Logged in as: {in_username}");
                        executer.run_script();
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
        }

        private void Exit_Click(object sender, RoutedEventArgs e)
        {
            executer.kill_script();
            Environment.Exit(0);
        }
    }
}