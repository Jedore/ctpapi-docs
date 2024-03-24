<p>请求RULE合约保证金参数查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYRULEINSTRPARAMETER/">OnRspQryRULEInstrParameter</a></p>
<span class="anchor" id="5499073e-7ffe-4312-a705-e36b9092763a"></span>
## 1.函数原型
<p>virtual int ReqQryRULEInstrParameter(CThostFtdcQryRULEInstrParameterField *pQryRULEInstrParameter, int nRequestID) = 0;</p>
<span class="anchor" id="35cf668d-e22e-4cf8-bcef-c68156319964"></span>
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
<span class="anchor" id="ba40bdb1-097d-47a1-9874-414842ce72d2"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="d09f839f-3ea3-46a2-a4b9-48ce4e717279"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="09d1a275-3db5-4f9f-b07e-cb38c11615b9"></span>
## 5.FAQ
<p>无</p>
