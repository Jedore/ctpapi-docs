<p>请求查询交易所</p>
<p>响应: <a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYEXCHANGE/">OnRspQryExchange</a></p>
<span class="anchor" id="a95bc1e8-4424-4f6a-9bad-db7a45e013c6"></span>
## 1.函数原型
<p>virtual int ReqQryExchange(CThostFtdcQryExchangeField *pQryExchange, int nRequestID) = 0;</p>
<span class="anchor" id="4dbae0fc-c992-4b0f-a5d6-a0d32c220c3c"></span>
## 2.参数
<p>pQryExchange：查询交易所</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcExchangeIDType</td>
<td style="TEXT-ALIGN: left;">ExchangeID</td>
<td style="TEXT-ALIGN: left;">交易所代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="17329145-7a9a-4754-8851-99462f50a008"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="158a5e44-9af6-4aa1-9666-84a13af3a220"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="b5c553b8-effd-41bc-b968-339c47efe561"></span>
## 5.FAQ
<p>无</p>
