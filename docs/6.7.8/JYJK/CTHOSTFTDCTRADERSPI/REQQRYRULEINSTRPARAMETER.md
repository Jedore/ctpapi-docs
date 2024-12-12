<p>请求RULE合约保证金参数查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYRULEINSTRPARAMETER/">OnRspQryRULEInstrParameter</a></p>
<span class="anchor" id="f2435e07-08e6-4c26-b573-ead6431e3441"></span>
## 1.函数原型
<p>virtual int ReqQryRULEInstrParameter(CThostFtdcQryRULEInstrParameterField *pQryRULEInstrParameter, int nRequestID) = 0;</p>
<span class="anchor" id="5eeb6970-2637-4a93-805c-1a5f8178f49c"></span>
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
<span class="anchor" id="5919f7fc-946b-420f-928e-75e3056bcdcf"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="3f517eb1-8827-4afc-8015-e4e7f3a2d14a"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="94fccf5f-e124-42ad-b657-fcfef98bf72a"></span>
## 5.FAQ
<p>无</p>
