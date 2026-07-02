#include <stdio.h>
#include <string.h>

char *longestPalindrome(char *s)
{
    int size_of_s = strlen(s);
    int inicio, fim;
    int max_size = 0;
    int max_ini, max_fim;

    for (int i = 0; i < size_of_s; i++)
    {

        inicio = i, fim = i;

        while (inicio >= 0 && fim < size_of_s && s[inicio] == s[fim])
        {
            inicio--;
            fim++;
        }

        int size_impar = fim - inicio - 1;

        if (max_size < size_impar)
        {
            max_size = size_impar;
            max_ini = inicio + 1;
            max_fim = fim;
        }

        inicio = i, fim = i + 1;

        while (inicio >= 0 && fim < size_of_s && s[inicio] == s[fim])
        {
            inicio--;
            fim++;
        }

        int size_par = fim - inicio - 1;

        if (max_size < size_par)
        {
            max_size = size_par;
            max_ini = inicio + 1;
            max_fim = fim;
        }
    }

    s[max_ini + max_size] = '\0';

    return &s[max_ini];
}