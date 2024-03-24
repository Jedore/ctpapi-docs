<p>请求查询产品组</p>
<p>响应: OnRspQryProductGroup</p>
<span class="anchor" id="0ea3d07d-ac55-486d-aa05-393c21d4c3fd"></span>
## 1.函数原型
<p>virtual int ReqQryProductGroup(CThostFtdcQryProductGroupField *pQryProductGroup, int nRequestID) = 0;</p>
<span class="anchor" id="b8edd141-75a4-4bb5-af3a-c0c424d26cc5"></span>
## 2.参数
<p>pQryProductGroup：查询产品组</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">ProductID</td>
<td style="TEXT-ALIGN: left;">产品代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcExchangeIDType</td>
<td style="TEXT-ALIGN: left;">ExchangeID</td>
<td style="TEXT-ALIGN: left;">交易所代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcOldInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">reserve1</td>
<td style="TEXT-ALIGN: left;">保留的无效字段</td>
<td style="TEXT-ALIGN: left;">否</td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="be55754b-f318-4910-936f-f59869702a0c"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="038fec78-0ff5-482e-b8c3-8a640589775b"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="4ab36c6e-4bb4-4f75-aa8e-d3c121d395cc"></span>
## 5.FAQ
<p>无</p>
