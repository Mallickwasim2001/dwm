public class Kmeans
{
public static void main(String args[])
{ int arr[] = {15,15,16,19,19,20,20,21,22,28,35,40,41,42,43,44,60,61,65}; // initial
data int i, m1, m2, a, b, n = 0;
boolean flag; 
float sum1, 
sum2; m1 = 20; 
m2 = 40;
int cluster1[] = new int[arr.length], cluster2[] = new 
int[arr.length]; do { sum1 = 0; sum2 = 0; cluster1 = new
int[arr.length]; cluster2 = new int[arr.length]; n++; int k
= 0, j = 0;
for (i = 0; i < arr.length; i++) { if
(Math.abs(arr[i] - m1) <= Math.abs(arr[i] - m2)) { cluster1[k]
= arr[i];
k++;
} else {
cluster2[j] = arr[i];
j++;
}
}
System.out.println(
); for (i = 0; i < k; i++) 
{
sum1 = sum1 + cluster1[i];
}
for (i = 0; i < j; i++) 
{ sum2 = sum2 + 
cluster2[i];
}
//printing Centroids/Means\
System.out.println("m1=" + m1 + " 
m2=" +
m2+"\n"); a = m1; b = 
m2; m1 = Math.round(sum1 
/ k);
m2 = Math.round(sum2 / 
j); flag = !(m1 == a && 
m2 == b);
System.out.println("After iteration " + n + " , Cluster 1 :\n"); //printing the 
clusters of each iteration
for (i = 0; i < cluster1.length; i++) { if(cluster1[i]!=0) 
System.out.print(cluster1[i] + "\t");
else System.out.print("\t");
}
System.out.println("\n");
System.out.println("After iteration " + n + " , Cluster 2 :\n");
for (i = 0; i < cluster2.length; i++)
{ if(cluster2[i]!=0)
System.out.print(cluster2[i] + "\t"); else 
System.out.print("\t");
}
} while (flag);
System.out.println("\nFinal cluster 1 :\n"); // final lusters 
for (i = 0; i < cluster1.length; i++)
{ if(cluster1[i]!=0)
System.out.print(cluster1[i] + "\t"); else 
System.out.print("\t");
}
System.out.println(); 
System.out.println("Final cluster 2 
:\n");
for (i = 0; i < cluster2.length; 
i++) { if(cluster2[i]!=0)
System.out.print(cluster2[i] + 
"\t"); else System.out.print("\t");
}
}
}
