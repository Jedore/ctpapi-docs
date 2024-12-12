<p>请求SPMM合约参数查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYSPMMINSTPARAM/">OnRspQrySPMMInstParam</a></p>
<span class="anchor" id="3cc8afd8-20e0-49d0-beb7-e25031363378"></span>
## 1.函数原型
<p>virtual int ReqQrySPMMInstParam(CThostFtdcQrySPMMInstParamField *pQrySPMMInstParam, int nRequestID) = 0;</p>
<span class="anchor" id="f34ceb3c-5794-4c92-bf63-31b4f7b8b839"></span>
## 2.参数
<p>pQrySPMMInstParam：SPMM合约参数查询</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">InstrumentID</td>
<td style="TEXT-ALIGN: left;">合约代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="34ae3ad1-c963-45c5-bc60-7b55dafa8d6f"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="04499906-8fb7-4128-aedb-ce024c678ac2"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="cd0ffa83-b791-4910-81e6-3452d74753ae"></span>
## 5.FAQ
<p>无</p>
