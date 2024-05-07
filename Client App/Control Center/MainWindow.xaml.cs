using System.Diagnostics;
using System.IO;
using System.Windows;
using Control_Center.Model;


namespace Control_Center
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        private Process Server;
        private PythonExecuter executer;

        public MainWindow()
        {
            executer = new PythonExecuter();
            Server = new Process();
            InitializeComponent();
        }

        private void Register_Click(object sender, RoutedEventArgs e)
        {
            string password = Microsoft.VisualBasic.Interaction.InputBox("Please enter a password!", "Register", "", 0, 0);
            if (password != "" ) {
                string filePath = AppDomain.CurrentDomain.BaseDirectory;
                filePath = filePath.Replace("\\bin\\Debug\\net8.0-windows", "");
                Directory.SetCurrentDirectory(filePath);
                File.Create("Persistence/Registered.txt").Close();
            }
        }

        private void Unregister_Click(object sender, RoutedEventArgs e)
        { }

        private void Connect_Click(object sender, RoutedEventArgs e)
        {
            string filePath = AppDomain.CurrentDomain.BaseDirectory;
            filePath = filePath.Replace("\\bin\\Debug\\net8.0-windows", "");
            Directory.SetCurrentDirectory(filePath);
            if (File.Exists("Persistence/Registered.txt"))
            {
                executer.run_script();
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