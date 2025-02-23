#include <iostream>
#include <math.h>
#include <stdio.h>
#include <windows.h>
#include <omp.h>
#include <time.h>
#include <fstream>
using namespace std;

double LiToDouble(LARGE_INTEGER x);
double GetTime();
void ParallelFindPrimes(long long int n, bool *a);
void SerialFindPrimes(long long int n, bool *a);
void TestResult(long long int n, bool *a);
void PrintPrimeInFile(long long int n, bool *a, string FileName);

int main()
{
    long long int n;
    int p;
    double Start, Finish, Duration_Serial, Duration_Parallel, Efficiency;
    bool *Result_Serial;
    bool *Result_Parallel;

    cout << "Parallel program to find primes less than or equal to n\n";
    cout << "Enter the natural number n: ";
    cin >> n;

    Result_Serial = new bool[n + 1];
    Result_Parallel = new bool[n + 1];

    Start = GetTime();
    SerialFindPrimes(n, Result_Serial);
    Finish = GetTime();
    Duration_Serial = Finish - Start;

    Start = GetTime();
    ParallelFindPrimes(n, Result_Parallel);
    Finish = GetTime();
    Duration_Parallel = Finish - Start;

    #pragma omp parallel
    p = omp_get_num_threads();
    cout << "omp_get_num_threads : " << p;

    Efficiency = Duration_Serial / (Duration_Parallel * p);

    TestResult(n, Result_Parallel);
    PrintPrimeInFile(n, Result_Serial, "official_output.txt");

    cout << "\n\nTime of execution serial: " << Duration_Serial;
    cout << "\n\nTime of execution parallel: " << Duration_Parallel;
    cout << "\n\nEfficiency of execution: " << Efficiency * 100 << "%";

    delete[] Result_Serial;
    delete[] Result_Parallel;

    return 0;
}

void ParallelFindPrimes(long long int n, bool *a)
{
    long long int m;
    #pragma omp parallel for
    for (long long int i = 2; i <= n; i++)
        a[i] = true;

    m = sqrt(n);
    #pragma omp parallel for schedule(dynamic, 1) shared(a)
    for (long long int i = 2; i <= m; i++)
        if (a[i] == true)
            for (long long int j = i * i; j <= n; j = j + i)
                a[j] = false;
    
}

void SerialFindPrimes(long long int n, bool *a)
{
    double m;

    for (long long int i = 2; i <= n; i++)
        a[i] = true;
    
   
    m = sqrt(n);
    for (long long int i = 2; i <= m; i++)
        if (a[i] == true)
            for (int j = i * i; j <= n; j = j + i)
                a[j] = false;
         
}

void TestResult(long long int n, bool *a)
{
    bool *b;
    b = new bool[n + 1];
    bool check = true;
    SerialFindPrimes(n, b);
    for (long long int i = 2; i <= n; i++)
    {
        if (a[i] != b[i])
        {
            check = false;
            break;
        }
    }
    if (check == false){
        cout << "\nThe results of serial and parallel algorithms "
                "are NOT identical. Check your code.";
    }
    else{
        cout << "\nThe results of serial and parallel algorithms are "
                "identical.";
    }
    delete[] b;
}

void PrintPrimeInFile(long long int n, bool *a, string FileName)
{
    long long int count = 1, i;
    fstream out;
    out.open(FileName, ios::out);
    out << "\nPrime numbers less than or equal " << n << ": \n";
    #pragma omp parallel for ordered
    for (i = 2; i <= n; i++)
    {
        #pragma omp ordered
        if (a[i] == true)
        {
            if (count % 10 == 0)
            {
                out << "\n";
            }
            count++;
            out << i << "\t";
        }
    }
    out.close();
}

double LiToDouble(LARGE_INTEGER x)
{
    double result = ((double)x.HighPart) * 4.294967296E9 + (double)((x).LowPart);
    return result;
}

double GetTime()
{
    LARGE_INTEGER lpFrequency, lpPerfomanceCount;
    QueryPerformanceFrequency(&lpFrequency);
    QueryPerformanceCounter(&lpPerfomanceCount);
    return LiToDouble(lpPerfomanceCount) / LiToDouble(lpFrequency);
}