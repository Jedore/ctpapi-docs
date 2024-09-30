<p>请求SPMM产品参数查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYSPMMPRODUCTPARAM/">OnRspQrySPMMProductParam</a></p>
<span class="anchor" id="2844dbe1-ecf7-451f-8294-b250cb6e9251"></span>
## 1.函数原型
<p>virtual int ReqQrySPMMProductParam(CThostFtdcQrySPMMProductParamField *pQrySPMMProductParam, int nRequestID) = 0;</p>
<span class="anchor" id="7f276c6f-920d-4297-bbf7-043df4d29b75"></span>
## 2.参数
<p>pQrySPMMProductParam：SPMM产品参数查询</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcSPMMProductIDType</td>
<td style="TEXT-ALIGN: left;">ProductID</td>
<td style="TEXT-ALIGN: left;">产品代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="9cd67f1c-3963-4a13-96e3-a96e7b77c61a"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="7dabde4b-9e96-49e2-94c3-004ff7d8843b"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="8bbe0008-e15b-4e73-84ea-8e1a6393a538"></span>
## 5.FAQ
<p>无</p>
