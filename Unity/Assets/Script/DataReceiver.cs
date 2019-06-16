using System;
using System.Collections;
using System.Collections.Generic;
using System.IO.Ports;
using System.Threading;
using UnityEngine.SceneManagement;
using UnityEngine;
using static System.Net.Mime.MediaTypeNames;
using System.IO;
using System.Text.RegularExpressions;

public class DataReceiver : MonoBehaviour
{
    private SerialPort sp = null;//端口
    private Thread athread;
    private List<List<float>> sequence = new List<List<float>>();
    public GUISkin mySkin;
    private int show = 0;
    private bool flag1 = false;
    private bool flag2 = false;
    private bool isOpen = false;
    private bool isSuccess = false;
    private bool isFailed = false;
    private bool isBegin = false;
    private int result = 0;
    private string condition = "";
    private string title = "";
    private string tips = "";
    private AudioSource _audioSource = null;

    private void Start()
    {
        InitPort("COM3", 9600);
        
    }

    void Update()
    {
        if (show == 1)
        {
            isOpen = true;
            OpenPort();
            condition = "初始化中！";
            print("串口已打开！开始读取数据！");
            StartReadData();
            show = 0;
        }
        if (show == 2)
        {
            flag1 = false;
            flag2 = false;
            isOpen = false;
            ClosePort();
            condition = "读取数据结束！";
            print("串口已关闭！");
            show = 0;
            contrast(sequence);
        }

    }

    /// <summary>
    /// 初始化端口
    /// </summary>
    public void InitPort(string portName, int baudRate)
    {
        sp = new SerialPort("\\\\.\\" + portName, baudRate);
        sp.ReadTimeout = 400;
    }

    /// <summary>
    /// 打开端口
    /// </summary>
    public void OpenPort()
    {
        try
        {
            sp.Open();
        }
        catch (Exception ex)
        {
            Debug.Log(ex.Message);
        }
    }

    /// <summary>
    /// 关闭端口
    /// </summary>
    public void ClosePort()
    {
        try
        {
            sp.Close();
        }
        catch (Exception ex)
        {
            Debug.Log(ex.Message);
        }
    }

    /// <summary>
    /// 开始读取数据
    /// </summary>
    public void StartReadData()
    {
        athread = new Thread(new ThreadStart(ReadPortData));
        athread.IsBackground = true;
        athread.Start();
    }


    private void ReadPortData()
    {
        string line = "";
        while (isOpen)
        {
            char c;
            if (sp != null && sp.IsOpen)
            {
                try
                {
                    try
                    {
                        c = (char)sp.ReadByte();
                        if (c != '\n')
                        {
                            line += c;
                        }
                        else
                        {
                            processLine(line);
                            line = "";
                        }
                    }
                    catch (System.Exception ex)
                    {

                        Debug.Log(ex.Message);
                    }
                }
                catch (Exception ex)
                {
                    Debug.Log(ex.Message);
                }
            }
            else
            {
                Debug.LogError("请检查端口设置！");
                condition = "请检查端口设置！";
            }
        }
    }

    private void processLine(string line)
    {
        List<float> datapoint = new List<float>();
        string[] strArry = line.Split(',');
        List<string> strlist = new List<string>(strArry);
        if (strlist.Count != 20 || strlist.Contains("0.00"))
        {
            return;
        }
        flag1 = true;
        if (flag1 != flag2)
        {
            isBegin = true;
            condition = "开始读取数据!";
            flag2 = true;
        }
        int count = 0;
        foreach (string s in strArry)
        {
            datapoint.Add(float.Parse(s));
            count++;
        }
        Debug.Log(line);
        sequence.Add(datapoint);
    }

    public void contrast(List<List<float>> sequence)
    {
        List<List<List<float>>> fingers = new List<List<List<float>>>();
        List<List<List<float>>> spins = new List<List<List<float>>>();
        List<List<List<float>>> rolls = new List<List<List<float>>>();
        List<List<List<float>>> fingers_sample = new List<List<List<float>>>();
        List<List<List<float>>> spins_sample = new List<List<List<float>>>();
        List<List<List<float>>> rolls_sample = new List<List<List<float>>>();
        
        for (int i = 0; i < 5; i++)
        {
            fingers.Add(new List<List<float>>());
            spins.Add(new List<List<float>>());
            rolls.Add(new List<List<float>>());
            fingers_sample.Add(new List<List<float>>());
            spins_sample.Add(new List<List<float>>());
            rolls_sample.Add(new List<List<float>>());
        }
        
        for (int i = 0; i < sequence.Count; i++)
        {
            List<float> temp = sequence[i];
            for (int j = 0; j < temp.Count; j++)
            {
                for (int k = 0; k < 5; k++)
                {
                    List<float> finger = new List<float>();
                    List<float> spin = new List<float>();
                    List<float> roll = new List<float>();
                    float x = temp[3 * k] * Mathf.PI / 180;
                    float y = temp[3 * k + 1] * Mathf.PI / 180;
                    float z = temp[3 * k + 2];
                    finger.Add(Mathf.Cos(x) * Mathf.Cos(y));
                    finger.Add(Mathf.Sin(x) * Mathf.Cos(y));
                    finger.Add(Mathf.Sin(y));
                    spin.Add(z);
                    roll.Add(temp[15 + k]);
                    fingers[k].Add(finger);
                    spins[k].Add(spin);
                    rolls[k].Add(roll);
                }
            }
        }
        
        string[] strs = File.ReadAllLines(@"C:\Users\27586\PycharmProjects\HCI\HCI-Project\origin\data\hou-data" + Selection.GetChoose() + "-1.txt");
        for (int i = 0; i < strs.Length; i++)
        {
            string[] str = Regex.Split(strs[i], ",", RegexOptions.IgnoreCase);
            for (int j = 0; j < 5; j++)
            {
                List<float> finger = new List<float>();
                List<float> spin = new List<float>();
                List<float> roll = new List<float>();
                float x = float.Parse(str[3 * j + 1]) * Mathf.PI / 180;
                float y = float.Parse(str[3 * j + 2]) * Mathf.PI / 180;
                float z = float.Parse(str[3 * j + 3]);
                finger.Add(Mathf.Cos(x) * Mathf.Cos(y));
                finger.Add(Mathf.Sin(x) * Mathf.Cos(y));
                finger.Add(Mathf.Sin(y));
                spin.Add(z);
                roll.Add(float.Parse(str[16 + j]));
                fingers_sample[j].Add(finger);
                spins_sample[j].Add(spin);
                rolls_sample[j].Add(roll);
            }
        }
        float score = 0;
        for (int i = 0; i < 5; i++)
        {
            score = score + 1.8f * Contrast.DTW(fingers[i], fingers_sample[i]) / 180 + 0.3f * Contrast.DTW(spins[i], spins_sample[i]) / 180 + 0.9f * Contrast.DTW(rolls[i], rolls_sample[i]) / 200;
        }
        Debug.Log(score);
        if (score < 1.5)
        {
            result = 1;
            isSuccess = true;
        }
        else {
            result = 2;
            isFailed = true;
        }
        sequence.Clear();
    }

    void OnGUI()
    {
        GUI.skin = mySkin;
        if (GUI.Button(new Rect(50, 50, 75, 75), "", GUI.skin.GetStyle("Back")))
        {
            SceneManager.LoadScene("Selection");
        }
        switch (Selection.GetChoose())
        {
            case "1":
                title = "镊子抓取固体";
                tips = "Tips:除大拇指外其余四指基本平行";
                break;
            case "2":
                title = "往试管中加固体";
                tips = "Tips:五指基本不弯曲";
                break;
            case "3":
                title = "胶头滴管吸取液体";
                tips = "Tips:注意中指，无名指与小拇指的位置";
                break;
            case "4":
                title = "烧杯倒水";
                tips = "Tips:注意右掌心与烧杯右侧相贴";
                break;
            default:
                break;
        }
        GUI.Label(new Rect(175, 50, 200, 75), title, GUI.skin.GetStyle("Text"));
        GUI.Label(new Rect(90, 240, 250, 100), condition, GUI.skin.GetStyle("Text"));
        GUI.Label(new Rect(500, 400, 600, 100), tips, GUI.skin.GetStyle("Text"));
        if (GUI.Button(new Rect(90, 140, 100, 100), "", GUI.skin.GetStyle("Start")))
        {
            show = 1;
        }
        if (GUI.Button(new Rect(240, 140, 100, 100), "", GUI.skin.GetStyle("Pause")))
        {
            show = 2;
        }
        if (result == 1)
        {
            GUI.Button(new Rect(90, 350, 250, 100), "", GUI.skin.GetStyle("Passed"));
        }
        if (result == 2)
        {

            GUI.Button(new Rect(90, 325, 250, 150), "", GUI.skin.GetStyle("Failed"));
        }
        if (isBegin)
        {

            //添加 Audio Source 组件
            _audioSource = this.gameObject.AddComponent<AudioSource>();
            //加载 Audio Clip 对象
            AudioClip audioClip = Resources.Load<AudioClip>("begin");
            //播放声音
            _audioSource.clip = audioClip;
            _audioSource.Play(0);
            isBegin = !isBegin;
        }
        if (isSuccess)
        {

            //添加 Audio Source 组件
            _audioSource = this.gameObject.AddComponent<AudioSource>();
            //加载 Audio Clip 对象
            AudioClip audioClip = Resources.Load<AudioClip>("success");
            //播放声音
            _audioSource.clip = audioClip;
            _audioSource.Play(0);
            isSuccess = !isSuccess;
        }
        if (isFailed)
        {

            //添加 Audio Source 组件
            _audioSource = this.gameObject.AddComponent<AudioSource>();
            //加载 Audio Clip 对象
            AudioClip audioClip = Resources.Load<AudioClip>("failed");
            //播放声音
            _audioSource.clip = audioClip;
            _audioSource.Play(0);
            isFailed = !isFailed;
        }
    }
}