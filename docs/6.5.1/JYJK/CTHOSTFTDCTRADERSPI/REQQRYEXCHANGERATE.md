<p>请求查询汇率</p>
<p>响应：OnRspQryExchangeRate</p>
<span class="anchor" id="3bc320ee-ef39-4962-a12a-0d578d20aa0e"></span>
## 1.函数原型
<p>virtual int ReqQryExchangeRate(CThostFtdcQryExchangeRateField *pQryExchangeRate, int nRequestID) = 0;</p>
<span class="anchor" id="22deb88a-b273-40b1-9653-a65c9d5a09e8"></span>
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
<span class="anchor" id="8becad6a-4f3f-4dde-97bd-8ffcf289e572"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="4b2f9537-f44a-4a53-8efb-de76e371ce92"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="484a5c7e-8247-4308-8111-54ba8b16b4d1"></span>
## 5.FAQ
<p>无</p>
