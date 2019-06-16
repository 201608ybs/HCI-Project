using System.Collections;
using System.Collections.Generic;
using UnityEngine.SceneManagement;
using UnityEngine;

public class Selection : MonoBehaviour
{
    public GUISkin mySkin;
    static string choose = "";
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
        GUI.Label(new Rect(90, 50, 50, 400), "固" + "\n" + "定" + "\n" + "手" + "\n" + "势" + "\n" + "识" + "\n" + "别", GUI.skin.GetStyle("Text"));
        if (GUI.Button(new Rect(50, Screen.height - 125, 75, 75), "", GUI.skin.GetStyle("Back")))
        {
            SceneManager.LoadScene("SampleScene");
        }
        if (GUI.Button(new Rect(125, Screen.height - 125, 75, 75), "", GUI.skin.GetStyle("Next")))
        {
            SceneManager.LoadScene("Customize");
        }
        if (GUI.Button(new Rect(175, 50, 400, 200), "", GUI.skin.GetStyle("Level1")))
        {
            SceneManager.LoadScene("Gesture1");
            choose = "1";
        }
        if (GUI.Button(new Rect(625, 50, 400, 200), "", GUI.skin.GetStyle("Level2")))
        {
            SceneManager.LoadScene("Gesture2");
            choose = "2";
        }
        if (GUI.Button(new Rect(175, 300, 400, 200), "", GUI.skin.GetStyle("Level3")))
        {
            SceneManager.LoadScene("Gesture3");
            choose = "3";
        }
        if (GUI.Button(new Rect(625, 300, 400, 200), "", GUI.skin.GetStyle("Level4")))
        {
            SceneManager.LoadScene("Gesture4");
            choose = "4";
        }
    }

    public static string GetChoose() {
        return choose;
    }
}
