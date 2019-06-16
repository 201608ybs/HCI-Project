using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CustomCusor : MonoBehaviour
{
    public Texture2D myCusor;
    //单击鼠标
    public Texture2D myClickCusor;
    //宽度
    float width;
    //高度
    float height;

    private bool showClickCusor = false;//是否显示点击鼠标的图片

    // Start is called before the first frame update
    void Start()
    {
        Cursor.visible = false;
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetMouseButton(0))
        {
            showClickCusor = true;
        }
        else
        {
            showClickCusor = false;
        }
    }

    void OnGUI()
    {
        var mousePos = Input.mousePosition;
        if (!showClickCusor)
        {
            GUI.DrawTexture(new Rect(mousePos.x, Screen.height - mousePos.y, myCusor.width, myCusor.height), myCusor);

        }
        else
        {
            GUI.DrawTexture(new Rect(mousePos.x, Screen.height - mousePos.y, myClickCusor.width, myClickCusor.height), myClickCusor);
        }
        GUI.depth = -2;
    }
}
