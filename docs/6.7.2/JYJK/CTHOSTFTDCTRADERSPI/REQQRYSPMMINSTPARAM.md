<p>请求SPMM合约参数查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYSPMMINSTPARAM/">OnRspQrySPMMInstParam</a></p>
<span class="anchor" id="8b7ab893-c499-4c0d-b0d5-6f16c60c91e2"></span>
## 1.函数原型
<p>virtual int ReqQrySPMMInstParam(CThostFtdcQrySPMMInstParamField *pQrySPMMInstParam, int nRequestID) = 0;</p>
<span class="anchor" id="6eaa26fe-f91b-46c1-9c0f-4fed2f94d758"></span>
## 2.参数
<p>pQrySPMMInstParam：SPMM合约参数查询</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">InstrumentID</td>
<td style="TEXT-ALIGN: left;">合约代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="d79d6d6c-3fd3-468b-ba6b-5a72c752bf84"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="9ab74fda-3724-4e47-8b54-cc543bc1f821"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="7fcd67f9-1014-4b4d-b29f-92f3064118ef"></span>
## 5.FAQ
<p>无</p>
