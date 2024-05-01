using System.Windows;

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
        }
    }

}
