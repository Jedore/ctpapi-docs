<p>请求查询交易员报盘机，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYTRADEROFFER/">OnRspQryTraderOffer</a></p>
<span class="anchor" id="e923ef98-44c4-411b-869a-7fc979d6c4d0"></span>
## 1.函数原型
<p>virtual int ReqQryTraderOffer(CThostFtdcQryTraderOfferField *pQryTraderOffer, int nRequestID) = 0;</p>
<span class="anchor" id="af18fd1b-7f2b-4881-8613-e78e6a3c4b84"></span>
## 2.参数
<p>pQryTraderOffer：查询交易员报盘机</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcExchangeIDType</td>
<td style="TEXT-ALIGN: left;">ExchangeID</td>
<td style="TEXT-ALIGN: left;">交易所代码</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcParticipantIDType</td>
<td style="TEXT-ALIGN: left;">ParticipantID</td>
<td style="TEXT-ALIGN: left;">会员代码</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcTraderIDType</td>
<td style="TEXT-ALIGN: left;">TraderID</td>
<td style="TEXT-ALIGN: left;">交易所交易员代码</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="89ee5960-1b01-407d-a932-da4a63f1d76d"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="4237d8b8-45f8-4839-a188-041737cd07fa"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="44d64e6b-54dd-4246-9210-65d72aa087d6"></span>
## 5.FAQ
<p>无</p>
