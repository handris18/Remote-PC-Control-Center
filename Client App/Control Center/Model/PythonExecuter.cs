using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;

namespace Control_Center.Model
{
    public class PythonExecuter
    {
        Process p;

        private void run_cmd(string cmd, string args)
        {
            ProcessStartInfo start = new ProcessStartInfo();
            start.FileName = cmd;//cmd is full path to python.exe
            start.Arguments = args;//args is path to .py file and any cmd line args
            start.UseShellExecute = false;
            start.RedirectStandardOutput = true;
            using (Process process = Process.Start(start))
            {
                using (StreamReader reader = process.StandardOutput)
                {
                    string result = reader.ReadToEnd();
                    Console.Write(result);
                }
            }
        }

        public void run_script()
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

            p.StandardInput.WriteLine("py model\\Client.py");
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
