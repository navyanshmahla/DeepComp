# DeepComp

DeepComp is a hybrid framework that aims at achieving a lossless (if not lossy) data compression with more compression ratio that our usual data compression algorithms like Huffman encoding, LZ77 and LZ78. 

Particularly this GitHub repository is an implementation of <a href="https://link.springer.com/article/10.1007/s13369-022-06587-x">this research paper</a> where the authors aim to devise a much more robust compression system for real-time streaming over the network. 

This approach tends to unify deep learning algorithms with traditional Windows archivers to compress both numerical and image data. 

Autoencoders- a well-known deep learning architecture widely used for data compression, outperform traditional archivers in terms of compression ratio but fall short in terms of reconstruction error. To minimize the reconstruction error, an attention layer is proposed in the autoencoder used in DeepComp. The attention layer accomplishes this by impeding the transition of spatial locality of the input data points during its processing in the compression and decompression phase. DeepComp is evaluated using numerical and image-type atmospheric and oceanic data obtained from the National Centers for Environmental Prediction (NCEP), which operates under National Oceanic and Atmospheric Administration (NOAA), USA. The performance analysis illustrates the robustness of DeepComp in compressing both numeric and image datatypes. In terms of compression ratio, it outperforms Windows archivers by an average of 69% and multilayer autoencoders by 48%. DeepComp also outperforms the reconstruction performance of the multilayer autoencoder.
