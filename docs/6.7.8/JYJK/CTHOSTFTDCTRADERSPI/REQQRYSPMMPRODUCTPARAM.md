<p>请求SPMM产品参数查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYSPMMPRODUCTPARAM/">OnRspQrySPMMProductParam</a></p>
<span class="anchor" id="d26cc5b4-62e5-4b23-a386-4a7943750618"></span>
## 1.函数原型
<p>virtual int ReqQrySPMMProductParam(CThostFtdcQrySPMMProductParamField *pQrySPMMProductParam, int nRequestID) = 0;</p>
<span class="anchor" id="6323f3be-6de2-4f1c-984a-2d9c870b82bc"></span>
## 2.参数
<p>pQrySPMMProductParam：SPMM产品参数查询</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcSPMMProductIDType</td>
<td style="TEXT-ALIGN: left;">ProductID</td>
<td style="TEXT-ALIGN: left;">产品代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="0a589453-b6be-45ed-9b6e-693e2425874d"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="e63be1c4-5dde-406a-8d9c-a4a529eab38e"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="366e8c04-4b80-4e46-aae8-4216d1667f18"></span>
## 5.FAQ
<p>无</p>
