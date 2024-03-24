<p>请求查询产品报价汇率</p>
<p>响应: <a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYPRODUCTEXCHRATE/">OnRspQryProductExchRate</a></p>
<span class="anchor" id="df24e4cf-4610-4f97-b223-cee6b1a2db2e"></span>
## 1.函数原型
<p>virtual int ReqQryProductExchRate(CThostFtdcQryProductExchRateField *pQryProductExchRate, int nRequestID) = 0;</p>
<span class="anchor" id="c88fb245-f52b-4406-a993-c1b0dcf8e71e"></span>
## 2.参数
<p>pQryProductExchRate：产品报价汇率查询</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">ProductID</td>
<td style="TEXT-ALIGN: left;">产品代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcExchangeIDType</td>
<td style="TEXT-ALIGN: left;">ExchangeID</td>
<td style="TEXT-ALIGN: left;">交易所代码</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcOldInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">reserve1</td>
<td style="TEXT-ALIGN: left;">保留的无效字段</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="69cf5b6c-c537-411f-9861-7f48641d24a3"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="7800c1ba-6f55-4f33-baf2-ff4d055f35ea"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="9ac70c10-c5da-40d9-a753-0ec373f629d2"></span>
## 5.FAQ
<p>无</p>
