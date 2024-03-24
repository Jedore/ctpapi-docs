<p>请求查询交易所</p>
<p>响应: OnRspQryExchange</p>
<span class="anchor" id="2b0b1bff-bad4-4119-ba78-27771dd1041e"></span>
## 1.函数原型
<p>virtual int ReqQryExchange(CThostFtdcQryExchangeField *pQryExchange, int nRequestID) = 0;</p>
<span class="anchor" id="2f340fda-2e19-49da-b16f-7af0d9b9f1ac"></span>
## 2.参数
<p>pQryExchange：查询交易所</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcExchangeIDType</td>
<td style="TEXT-ALIGN: left;">ExchangeID</td>
<td style="TEXT-ALIGN: left;">交易所代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="add622a6-8388-4ebf-a69d-b4fdf8d128b3"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="684054d0-bd08-4211-add1-49703c954730"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="9a77f511-5dd4-42be-85f9-f8904662b18e"></span>
## 5.FAQ
<p>无</p>
