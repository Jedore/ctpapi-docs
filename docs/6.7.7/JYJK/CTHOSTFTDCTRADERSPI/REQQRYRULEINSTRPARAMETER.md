<p>请求RULE合约保证金参数查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYRULEINSTRPARAMETER/">OnRspQryRULEInstrParameter</a></p>
<span class="anchor" id="eba26f3e-87e0-44cb-91aa-7a80bc18854c"></span>
## 1.函数原型
<p>virtual int ReqQryRULEInstrParameter(CThostFtdcQryRULEInstrParameterField *pQryRULEInstrParameter, int nRequestID) = 0;</p>
<span class="anchor" id="29f0206c-e5ff-4410-9671-6d7fdd7fb17f"></span>
## 2.参数
<p>pQryRULEInstrParameter：RULE合约保证金参数查询</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcExchangeIDType</td>
<td style="TEXT-ALIGN: left;">ExchangeID</td>
<td style="TEXT-ALIGN: left;">交易所代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">InstrumentID</td>
<td style="TEXT-ALIGN: left;">合约代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<span class="anchor" id="a302a696-f000-4e0f-804a-0a0871f49b1f"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="8ef7ffd8-d459-49be-9159-ee571623cd74"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="bb29e3e5-0684-4b17-8780-b11c2a1a1235"></span>
## 5.FAQ
<p>无</p>
