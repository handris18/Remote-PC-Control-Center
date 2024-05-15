using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Windows.Controls;

namespace Control_Center.Model
{
    public class PythonExecuter
    {
        Process p;

        public void run_script(string UID)
        {
            string filePath = AppDomain.CurrentDomain.BaseDirectory;
            filePath = filePath.Replace("\\bin\\Debug\\net8.0-windows", "");
            Directory.SetCurrentDirectory(filePath);

            p = new Process();
            p.StartInfo = new ProcessStartInfo("CMD.exe")
            {
                //Arguments = "py model\\Client.py",
                RedirectStandardOutput = true,
                RedirectStandardInput = true,
                UseShellExecute = false,
                CreateNoWindow = false
            };
            p.Start();

            p.StandardInput.WriteLine("py model\\Client.py " + UID);
        }

        public void kill_script()
        {
            try {
                if (p != null)
                {
                    p.Kill();
                    foreach (var server in Process.GetProcessesByName("python"))
                    {
                        server.Kill();
                    }
                    p.Close();
                }
            } 
            catch {
            }
        }
    }
}
