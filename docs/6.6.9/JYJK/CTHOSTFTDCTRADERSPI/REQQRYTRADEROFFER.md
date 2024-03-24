<p>请求查询交易员报盘机，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYTRADEROFFER/">OnRspQryTraderOffer</a></p>
<span class="anchor" id="83b10ad3-38ca-4532-afb1-2ea815c00968"></span>
## 1.函数原型
<p>virtual int ReqQryTraderOffer(CThostFtdcQryTraderOfferField *pQryTraderOffer, int nRequestID) = 0;</p>
<span class="anchor" id="0abe259a-13cb-453c-ba80-dc704365df94"></span>
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
<span class="anchor" id="f393ac47-a0fb-4310-ae15-5ca377daa058"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="6b8fcc0b-b043-4ddd-9b8d-89926e00ea61"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="d71e22ed-7c90-46f3-aea1-2edcd9ce5b44"></span>
## 5.FAQ
<p>无</p>
