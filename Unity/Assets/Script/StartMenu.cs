using System.Collections;
using System.Collections.Generic;
using UnityEngine.SceneManagement;
using UnityEngine;

public class StartMenu : MonoBehaviour
{
    public GUISkin mySkin;
    private string info = "111";
    private bool showWindow = false;

    private Rect myWindow;
    public Texture2D quitButton;//退出界面

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    void OnGUI()
    {
        GUI.skin = mySkin;
        if (showWindow)
        {
            GUI.DrawTexture(new Rect(Screen.width / 2 - 300, Screen.height / 2 - 100, 598, 275), quitButton);
            if (GUI.Button(new Rect(Screen.width / 2 + 105, Screen.height / 2 + 25, 135, 135), "", GUI.skin.GetStyle("OK"))) {
                Application.Quit();//退出程序
            }
            if (GUI.Button(new Rect(Screen.width / 2 - 245, Screen.height / 2 + 25, 135, 135), "", GUI.skin.GetStyle("Close")))
            {
                showWindow = false;
            }
        }
        else {
            if (GUI.Button(new Rect(Screen.width - 150, Screen.height - 125, 100, 100), " ", GUI.skin.GetStyle("Quit")))
            {
                showWindow = true;
            }
            if (GUI.Button(new Rect(Screen.width / 2 - 150, Screen.height / 2 - 50, 300, 150), " ", GUI.skin.GetStyle("Play")))
            {
                SceneManager.LoadScene("Selection");
            }
        }
    }  

}
