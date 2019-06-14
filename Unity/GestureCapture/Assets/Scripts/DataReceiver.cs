using System;
using System.Collections;
using System.Collections.Generic;
using System.IO.Ports;
using System.Threading;
using UnityEngine;
using static System.Net.Mime.MediaTypeNames;

public class DataReceiver : MonoBehaviour
{
    private SerialPort sp = null;//端口
    private Thread athread;
    private List<float> datapoint = new List<float>();
    private List<List<float>> sequence = new List<List<float>>();

    private void Start()
    {
        InitPort("COM4", 57600);
        OpenPort();
        print("串口已打开！开始读取数据！");
        StartReadData();
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
        while (true)
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
            }
        }
    }

    private void processLine(string line)
    {
        string[] strArry = line.Split(',');
        List<string> strlist = new List<string>(strArry);
        if (strlist.Capacity != 20)
        {
            return;
        }
        int count = 0;
        foreach(string s in strArry)
        {
            datapoint.Add(float.Parse(s));
            //Debug.Log(datapoint[count]);
            count++;
        }
        sequence.Add(datapoint);
        // 验证数据个数正确
        //string debugStr = "";
        //for (int i = 0; i < datapoint.Count; ++i)
        //{
        //    if (i != datapoint.Count - 1)
        //    {
        //        debugStr += datapoint[i].ToString() + ",";
        //    }
        //    else
        //    {
        //        debugStr += datapoint[i].ToString();
        //    }
        //}
        //Debug.Log(debugStr);
        datapoint.Clear();
    }
}
