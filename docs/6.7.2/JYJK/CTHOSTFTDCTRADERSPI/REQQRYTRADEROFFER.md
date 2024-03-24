<p>请求查询交易员报盘机，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYTRADEROFFER/">OnRspQryTraderOffer</a></p>
<span class="anchor" id="5ef50c6b-4029-492c-a398-d87f26a38ef4"></span>
## 1.函数原型
<p>virtual int ReqQryTraderOffer(CThostFtdcQryTraderOfferField *pQryTraderOffer, int nRequestID) = 0;</p>
<span class="anchor" id="c4efcca4-c8f9-468e-b6a3-506f783337e1"></span>
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
<span class="anchor" id="8cb8cf8b-bd82-443f-809b-7bf62fc09fc7"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="96eb9825-152b-4c46-86a6-56a3c53de7cc"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="9c1ed396-430d-4d67-913b-e590c4913c3c"></span>
## 5.FAQ
<p>无</p>
