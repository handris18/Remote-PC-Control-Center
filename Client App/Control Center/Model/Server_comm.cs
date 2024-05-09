using Newtonsoft.Json;
using System.Net;
using System.Net.Http;
using System.Text;

namespace Control_Center.Model
{
    public class Server_comm
    {
        public bool success;
        public HttpStatusCode error_code;

        public Server_comm() 
        { 
            success = false;
        }

        public async void Send_to_Server(object data, string url)
        {
            success = false;

            // Serialize the JSON data
            var jsonData = JsonConvert.SerializeObject(data);


            // Create HttpClient instance
            using (var httpClient = new HttpClient())
            {
                var content = new StringContent(jsonData, Encoding.UTF8, "application/json");

                var response = await httpClient.PostAsync(url, content);

                if (response.IsSuccessStatusCode)
                {
                    success = true;
                }
                else
                {
                    error_code = response.StatusCode;
                    Console.WriteLine("Failed to send JSON data. Status code: " + response.StatusCode);
                }
            }
        }  
    }
}
