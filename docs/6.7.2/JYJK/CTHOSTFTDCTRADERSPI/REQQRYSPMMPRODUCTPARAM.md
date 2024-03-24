<p>请求SPMM产品参数查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYSPMMPRODUCTPARAM/">OnRspQrySPMMProductParam</a></p>
<span class="anchor" id="7afe573a-d7c1-4cf2-b784-aa74a671cdf0"></span>
## 1.函数原型
<p>virtual int ReqQrySPMMProductParam(CThostFtdcQrySPMMProductParamField *pQrySPMMProductParam, int nRequestID) = 0;</p>
<span class="anchor" id="2f8d0c7d-0f04-49d5-a40b-5b2af5ca50c1"></span>
## 2.参数
<p>pQrySPMMProductParam：SPMM产品参数查询</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcSPMMProductIDType</td>
<td style="TEXT-ALIGN: left;">ProductID</td>
<td style="TEXT-ALIGN: left;">产品代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="1d3f245a-d809-4251-9473-bb1eba7323b5"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="729e6ed7-9dfe-4eaa-8775-f26320f4f0b8"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="9f57ca86-8741-43af-9e2a-06331390c649"></span>
## 5.FAQ
<p>无</p>
