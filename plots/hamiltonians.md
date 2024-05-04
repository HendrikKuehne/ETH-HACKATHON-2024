The hamiltonians we plotted:

* 1st: $\hat{H} = -\sum v_i\frac{1-\hat{Z}_i}{2} \equiv \sum v_i\hat{Z}_i$
* 2nd: $\hat{H} = -\sum v_i\frac{1-\hat{Z}_i}{2} - \left(d_{\text{max}} - \sum d_i\frac{1-\hat{Z}_i}{2}\right) \equiv \sum (v_i-d_i)\hat{Z}_i$
* 3rd: $\hat{H} = -\sum \frac{v_i}{d_i}\frac{1-\hat{Z}_i}{2} \equiv \sum \frac{v_i}{d_i}\hat{Z}_i$
* 4th: $\hat{H} = -\left(1 - \frac{1}{d_{\text{max}}}\sum d_i\frac{1-\hat{Z}_i}{2}\right)\sum v_i\frac{1-\hat{Z}_i}{2}$
* 5ht: $\hat{H} = \text{softplus}\left(\frac{1}{d_{\text{max}}}\sum d_i\frac{1-\hat{Z}_i}{2}-1\right)-\sum v_i\frac{1-\hat{Z}_i}{2}$