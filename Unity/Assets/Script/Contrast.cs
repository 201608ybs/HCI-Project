using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Contrast : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        List<List<float>> sequence1 = new List<List<float>>();
        List<List<float>> sequence2 = new List<List<float>>();
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    static List<float> normalize(List<float> point) {
        float count = 0;
        for (int i = 0; i < point.Count; i++) {
            count += point[i] * point[i];
        }
        count = (float)Math.Sqrt(count);
        if (count != 0)
        {
            for (int i = 0; i < point.Count; i++)
            {
                point[i] /= count;
            }
        }
        return point;
    }

    static float cal_distance(List<float> point1, List<float> point2) {
        float count = 0;
        if (point1.Count == 3)
        {
            point1 = normalize(point1);
            point2 = normalize(point2);
            for (int i = 0; i < point1.Count; i++)
            {
                count += point1[i] * point2[i];
            }
            if (count > 1)
            {
                count = 1;
            }
            if (count < -1)
            {
                count = -1;
            }
            count = Mathf.Acos(count) * 180 / Mathf.PI;
        }
        else if (point1.Count == 1 && point1[0] > 180)
        {
            count = Mathf.Abs(point1[0] - point2[0]);
        }
        else
        {
            count = Mathf.Abs(point1[0] - point2[0]);
            if (count > 180)
            {
                count = 360 - count;
            }
        }
        return count; 
    }

    public static float DTW(List<List<float>> sequence1, List<List<float>> sequence2) {
        int r = sequence1.Count;
        int c = sequence2.Count;
        List<List<float>> D0 = new List<List<float>>();
        List<List<float>> D1 = new List<List<float>>();
        for (int i = 0; i <= r; i++) {
            List<float> temp = new List<float>();
            for (int j = 0; j <= c; j++)
            {
                if (i * j == 0 && i + j != 0)
                {
                    temp.Add(Mathf.Infinity);
                }
                else {
                    temp.Add(0);
                }
            }
            D0.Add(temp);
        }
        for (int i = 1; i <= r; i++)
        {
            List<float> temp = new List<float>();
            for (int j = 1; j <= c; j++)
            {
                D0[i][j] = cal_distance(sequence1[i - 1], sequence2[j - 1]);
                temp.Add(D0[i][j]);
            }
            D1.Add(temp);
        }
        for (int i = 0; i < r; i++)
        {
            for (int j = 0; j < c; j++)
            {
                D1[i][j] += Math.Min(D0[i][j], Math.Min(D0[i][j + 1], D0[i + 1][j]));
                D0[i + 1][j + 1] += Math.Min(D0[i][j], Math.Min(D0[i][j + 1], D0[i + 1][j]));
            }
        }
        int r_copy = r - 1;
        int c_copy = c - 1;
        int count = 1;
        while (r_copy > 0 || c_copy > 0) {
            if (D0[r_copy][c_copy] <= D0[r_copy + 1][c_copy] && D0[r_copy][c_copy] <= D0[r_copy][c_copy + 1])
            {
                r_copy--;
                c_copy--;
            }
            else if (D0[r_copy][c_copy + 1] < D0[r_copy][c_copy] && D0[r_copy][c_copy + 1] <= D0[r_copy + 1][c_copy])
            {
                r_copy--;
            }
            else
            {
                c_copy--;
            }
            count++;
        }
        return D1[r - 1][c - 1] / count;
    }
}
