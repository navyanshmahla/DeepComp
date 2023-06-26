# DeepComp

DeepComp is a hybrid framework that aims at achieving a lossless (if not lossy) data compression with more compression ratio that our usual data compression algorithms like Huffman encoding, LZ77 and LZ78. 

Particularly this GitHub repository is an implementation of <a href="https://link.springer.com/article/10.1007/s13369-022-06587-x">this research paper</a> where the authors aim to devise a much more robust compression system for real-time streaming over the network. 
This proposed study aims to fulfill this research gap by developing a new hybrid deep learning framework named DeepComp which is an atten- tion based autoencoder architecture integrated with WinRAR archiver to achieve efficient numeric and image data com- pression for the atmospheric and oceanic data obtained from NCEP.
This approach tends to unify deep learning algorithms with traditional Windows archivers to compress both numerical and image data. 

Autoencoders are a type of deep learning architecture commonly used for compressing data. While they excel in achieving high compression ratios compared to traditional archivers, they tend to struggle in minimizing reconstruction errors. To address this limitation, a novel approach called DeepComp introduces an attention layer within the autoencoder. This attention layer specifically focuses on preserving the spatial locality of the input data points during compression and decompression processes.

To evaluate the effectiveness of DeepComp, numerical and image-based atmospheric and oceanic data obtained from the National Centers for Environmental Prediction (NCEP), which operates under the National Oceanic and Atmospheric Administration (NOAA) in the USA, were utilized. The performance analysis demonstrated the robustness of DeepComp in compressing various data types, including both numeric and image data.

In terms of compression ratio, DeepComp outperforms commonly used Windows archivers by an average of 69% and surpasses multilayer autoencoders by 48%. Moreover, DeepComp achieves superior reconstruction performance compared to traditional multilayer autoencoders.

Essentially, DeepComp introduces an attention layer to enhance the compression and reconstruction capabilities of autoencoders. It demonstrates impressive compression ratios and reconstruction performance, outperforming conventional archivers and traditional autoencoders when applied to diverse datasets, including numerical and image-based atmospheric and oceanic data.

**BLOG COMING SOON!!!!**
