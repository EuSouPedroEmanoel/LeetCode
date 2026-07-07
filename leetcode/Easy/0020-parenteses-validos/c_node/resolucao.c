#include <stdio.h>
#include <stdbool.h>

bool isValid(char *s)
{
    char vetor[10000];
    int i = 0;
    int writer = 0;
    while (s[i] != '\0')
    {
        switch (s[i])
        {
        case '{':
            vetor[writer] = '}';
            writer++;
            break;
        case '(':
            vetor[writer] = ')';
            writer++;
            break;
        case '[':
            vetor[writer] = ']';
            writer++;
            break;
        default:
            if (writer <= 0 || vetor[writer - 1] != s[i])
            {
                return false;
            }
            else
            {
                writer--;
            }
        }

        i++;
    }

    if (writer == 0)
        return true;

    else
        return false;
}