begin int x, y, power;
      float z;
      input(x, y);
      if(y<0)
      power = -y;
      else power = y;
      z=1;
      while(power!=0)
      {    z=z*x;
           power=power-1;
      } if(y<0)
      z=1/z;
      output(z);
      end