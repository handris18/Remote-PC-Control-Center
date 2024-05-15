using Newtonsoft.Json;
using System;
using System.IO;
using System.Net;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Net.Http.Json;
using System.Reflection.Metadata;
using System.Text;
using System.Windows;

namespace Control_Center.Model
{
    public class Server_comm
    {
        public HttpStatusCode error_code;

        public Server_comm(){}

        public async Task<bool> Send_to_Server(Dictionary<string, string> data, string url)
        {
            string filePath = AppDomain.CurrentDomain.BaseDirectory;
            filePath = filePath.Replace("\\bin\\Debug\\net8.0-windows", "");
            Directory.SetCurrentDirectory(filePath);

            using (var httpClient = new HttpClient())
            {
                httpClient.DefaultRequestHeaders.Clear();
                httpClient.DefaultRequestHeaders.ExpectContinue = false;
                httpClient.DefaultRequestHeaders.Add("Accept", "application/json");

                HttpResponseMessage response = null;

                using (var request = new HttpRequestMessage(HttpMethod.Post, url))
                {
                    request.Headers.Accept.Add(new MediaTypeWithQualityHeaderValue("application/json"));
                    var jsonData = JsonConvert.SerializeObject(data).ToString();
                    var content = new StringContent(jsonData, Encoding.UTF8, "application/json");
                    request.Content = content;
                    response = await httpClient.SendAsync(request);
                    //var token = response.Content
                }

                if (response.IsSuccessStatusCode)
                {
                    return true;
                }
                else
                {
                    error_code = response.StatusCode;
                    return false;
                }
            }
        }  
    }
}
