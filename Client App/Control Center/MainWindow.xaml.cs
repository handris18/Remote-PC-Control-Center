using System.Diagnostics;
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

        private void Connect_Click(object sender, RoutedEventArgs e)
        {
            executer.run_script();
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