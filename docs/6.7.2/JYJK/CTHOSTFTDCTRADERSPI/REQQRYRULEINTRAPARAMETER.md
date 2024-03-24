<p>请求RULE品种内对锁仓折扣参数查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYRULEINTRAPARAMETER/">OnRspQryRULEIntraParameter</a></p>
<span class="anchor" id="13c5218a-7366-4020-b826-109cd9917eed"></span>
## 1.函数原型
<p>virtual int ReqQryRULEIntraParameter(CThostFtdcQryRULEIntraParameterField *pQryRULEIntraParameter, int nRequestID) = 0;</p>
<span class="anchor" id="523a33db-7a2b-4179-aa80-63bbc33b14ef"></span>
## 2.参数
<p>pQryRULEIntraParameter：RULE品种内对锁仓折扣参数查询</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcExchangeIDType</td>
<td style="TEXT-ALIGN: left;">ExchangeID</td>
<td style="TEXT-ALIGN: left;">交易所代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">ProdFamilyCode</td>
<td style="TEXT-ALIGN: left;">品种代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<span class="anchor" id="07204145-50c2-406b-8794-9d5e6584c5b4"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="296761e6-4728-4c8c-9789-7af8c1a43abd"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="f343804d-83d4-42a5-ab79-423805dd6e2e"></span>
## 5.FAQ
<p>无</p>
