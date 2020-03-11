bool isValid(char * s){
    int len = strlen(s);

    if (len%2 != 0)
    {
      return false;
    }

    char *array = malloc(len); int idx = 0; char ch, back;

    for(int i = 0; i < len; i++)
    {
      ch = s[i];
      if(ch == '(' || ch == '[' || ch =='{')
      {
        if (idx >= len/2)
        {
          return false;
        }
        else
        {
          array[idx++] = ch;
          printf(idx);
        }
      }
      else
      {
        if (idx == 0)
        {
          return false;
        }
        back = array[idx-1];
        if((back == '(' && ch == ')')
            || (back == '[' && ch == ']')
            || (back == '{' && ch == '}') )
        {
            idx--;
        }
      }
      }
      return idx == 0;
    }
