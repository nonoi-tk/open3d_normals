# open3d_normals

open3dにおける法線ベクトル推定の可視化。

## 検証方法

半円型の点群データを作成して各点の法線ベクトル推定を実施。

## 結果

各点の近傍からなるジオメトリに対して垂直に伸びていることが確認できる。
http://www.open3d.org/docs/release/python_api/open3d.geometry.PointCloud.html


![法線ベクトル推定１](https://github.com/nonoi-tk/open3d_normals/blob/main/%E6%B3%95%E7%B7%9A%E3%83%99%E3%82%AF%E3%83%88%E3%83%AB%E6%8E%A8%E5%AE%9A1.png)
![法線ベクトル推定2](https://github.com/nonoi-tk/open3d_normals/blob/main/%E6%B3%95%E7%B7%9A%E3%83%99%E3%82%AF%E3%83%88%E3%83%AB%E6%8E%A8%E5%AE%9A2.png)
