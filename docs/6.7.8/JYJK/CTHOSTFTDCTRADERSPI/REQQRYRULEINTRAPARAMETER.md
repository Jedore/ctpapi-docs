<p>请求RULE品种内对锁仓折扣参数查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYRULEINTRAPARAMETER/">OnRspQryRULEIntraParameter</a></p>
<span class="anchor" id="e9885615-9cd8-4f1c-888e-b57abbfc5aea"></span>
## 1.函数原型
<p>virtual int ReqQryRULEIntraParameter(CThostFtdcQryRULEIntraParameterField *pQryRULEIntraParameter, int nRequestID) = 0;</p>
<span class="anchor" id="899cdcd7-9e52-49fa-9e99-88ce1cc167b4"></span>
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
<span class="anchor" id="4c4fd1e7-7cdc-41b6-b204-18eabb320f5d"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="921d695b-2e00-4d99-9c44-76d79f03a928"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="63ebfdd4-4a0a-42f4-b0bb-28dacb15fecd"></span>
## 5.FAQ
<p>无</p>
