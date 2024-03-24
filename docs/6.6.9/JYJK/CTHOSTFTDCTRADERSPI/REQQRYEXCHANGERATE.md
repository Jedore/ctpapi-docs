<p>请求查询汇率</p>
<p>响应：<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYEXCHANGERATE/">OnRspQryExchangeRate</a></p>
<span class="anchor" id="695c491b-83f8-4cdd-9466-0b3ad6d83479"></span>
## 1.函数原型
<p>virtual int ReqQryExchangeRate(CThostFtdcQryExchangeRateField *pQryExchangeRate, int nRequestID) = 0;</p>
<span class="anchor" id="0a9b4bf2-9628-45e0-8298-76d958f14e2c"></span>
## 2.参数
<p>pQryExchangeRate：查询汇率</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcBrokerIDType</td>
<td style="TEXT-ALIGN: left;">BrokerID</td>
<td style="TEXT-ALIGN: left;">经纪公司代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcCurrencyIDType</td>
<td style="TEXT-ALIGN: left;">FromCurrencyID</td>
<td style="TEXT-ALIGN: left;">源币种</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcCurrencyIDType</td>
<td style="TEXT-ALIGN: left;">ToCurrencyID</td>
<td style="TEXT-ALIGN: left;">目标币种</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="d0c1469d-a345-4f39-97a2-cb30b3d34b99"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="3168d10c-60b7-49c5-8f27-9d0060c9b395"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="0e28e5c2-8709-4548-a600-75b93f52397d"></span>
## 5.FAQ
<p>无</p>
