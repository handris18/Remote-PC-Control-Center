namespace Remote_PC_Control_Center
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            menuStrip1 = new MenuStrip();
            actionsToolStripMenuItem = new ToolStripMenuItem();
            registerDeviceToolStripMenuItem = new ToolStripMenuItem();
            deleteRegistrationToolStripMenuItem = new ToolStripMenuItem();
            connectToServerToolStripMenuItem = new ToolStripMenuItem();
            disconnectToolStripMenuItem = new ToolStripMenuItem();
            menuStrip1.SuspendLayout();
            SuspendLayout();
            // 
            // menuStrip1
            // 
            menuStrip1.Items.AddRange(new ToolStripItem[] { actionsToolStripMenuItem });
            menuStrip1.Location = new Point(0, 0);
            menuStrip1.Name = "menuStrip1";
            menuStrip1.Size = new Size(800, 24);
            menuStrip1.TabIndex = 0;
            menuStrip1.Text = "menuStrip1";
            // 
            // actionsToolStripMenuItem
            // 
            actionsToolStripMenuItem.DropDownItems.AddRange(new ToolStripItem[] { registerDeviceToolStripMenuItem, deleteRegistrationToolStripMenuItem, connectToServerToolStripMenuItem, disconnectToolStripMenuItem });
            actionsToolStripMenuItem.Name = "actionsToolStripMenuItem";
            actionsToolStripMenuItem.Size = new Size(122, 20);
            actionsToolStripMenuItem.Text = "Actions";
            // 
            // registerDeviceToolStripMenuItem
            // 
            registerDeviceToolStripMenuItem.Name = "registerDeviceToolStripMenuItem";
            registerDeviceToolStripMenuItem.Size = new Size(180, 22);
            registerDeviceToolStripMenuItem.Text = "Register device";
            // 
            // deleteRegistrationToolStripMenuItem
            // 
            deleteRegistrationToolStripMenuItem.Name = "deleteRegistrationToolStripMenuItem";
            deleteRegistrationToolStripMenuItem.Size = new Size(180, 22);
            deleteRegistrationToolStripMenuItem.Text = "Delete registration";
            // 
            // connectToServerToolStripMenuItem
            // 
            connectToServerToolStripMenuItem.Name = "connectToServerToolStripMenuItem";
            connectToServerToolStripMenuItem.Size = new Size(180, 22);
            connectToServerToolStripMenuItem.Text = "Connect";
            // 
            // disconnectToolStripMenuItem
            // 
            disconnectToolStripMenuItem.Name = "disconnectToolStripMenuItem";
            disconnectToolStripMenuItem.Size = new Size(180, 22);
            disconnectToolStripMenuItem.Text = "Disconnect";
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(800, 450);
            Controls.Add(menuStrip1);
            MainMenuStrip = menuStrip1;
            Name = "Form1";
            Text = "Form1";
            menuStrip1.ResumeLayout(false);
            menuStrip1.PerformLayout();
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private MenuStrip menuStrip1;
        private ToolStripMenuItem actionsToolStripMenuItem;
        private ToolStripMenuItem registerDeviceToolStripMenuItem;
        private ToolStripMenuItem deleteRegistrationToolStripMenuItem;
        private ToolStripMenuItem connectToServerToolStripMenuItem;
        private ToolStripMenuItem disconnectToolStripMenuItem;
    }
}
