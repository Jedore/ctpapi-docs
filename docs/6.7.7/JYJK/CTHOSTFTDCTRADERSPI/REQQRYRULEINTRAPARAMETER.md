<p>请求RULE品种内对锁仓折扣参数查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYRULEINTRAPARAMETER/">OnRspQryRULEIntraParameter</a></p>
<span class="anchor" id="2672755a-d17d-43f3-b365-34cd60fa3c2b"></span>
## 1.函数原型
<p>virtual int ReqQryRULEIntraParameter(CThostFtdcQryRULEIntraParameterField *pQryRULEIntraParameter, int nRequestID) = 0;</p>
<span class="anchor" id="898fc828-1bd7-4c73-8ab7-65d3d3c9bce6"></span>
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
<span class="anchor" id="25059841-c0c0-4c59-ac83-7308fcd9806f"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="2323c2f7-45d0-4a08-8589-c6499215b988"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="95b397aa-d6bf-418b-b5d7-711b9697b002"></span>
## 5.FAQ
<p>无</p>
