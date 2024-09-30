<p>请求查询交易员报盘机，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYTRADEROFFER/">OnRspQryTraderOffer</a></p>
<span class="anchor" id="5e62caaa-711a-4f2f-9557-864cd58ebf87"></span>
## 1.函数原型
<p>virtual int ReqQryTraderOffer(CThostFtdcQryTraderOfferField *pQryTraderOffer, int nRequestID) = 0;</p>
<span class="anchor" id="55b53e58-a990-473f-8bd2-70a53fa43401"></span>
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
<span class="anchor" id="a3f3ef9c-b3f4-4bba-b955-3dfd2a716f26"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="a9288279-e942-4bee-b827-0d19c5794766"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="25c9ece5-096e-4a04-bb1c-10ae9cecafa2"></span>
## 5.FAQ
<p>无</p>
