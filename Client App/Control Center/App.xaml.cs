using System.IO;
using System.Windows;
using System.Windows.Shapes;

namespace Control_Center
{
    /// <summary>
    /// Interaction logic for App.xaml
    /// </summary>
    public partial class App : Application
    {
        private MainWindow _view;

        public App()
        {
            Startup += new StartupEventHandler(App_Startup);
        }

        private void App_Startup(object sender, StartupEventArgs e)
        {
            _view = new MainWindow();
            //_view.DataContext = ;
            //_view.Closing += new System.ComponentModel.CancelEventHandler(View_Closing);
            _view.Show();

            string filePath = AppDomain.CurrentDomain.BaseDirectory;
            filePath = filePath.Replace("\\bin\\Debug\\net8.0-windows", "");
            Directory.SetCurrentDirectory(filePath);

            if (!File.Exists("Persistence/UID.txt"))
            {
                Guid guid = Guid.NewGuid();
                string uid = guid.ToString();
                using (StreamWriter writetext = new StreamWriter("Persistence/UID.txt"))
                {
                    writetext.WriteLine(uid);
                }
            }
        }
    }

}
