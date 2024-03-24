<p>请求查询产品组</p>
<p>响应: <a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYPRODUCTGROUP/">OnRspQryProductGroup</a></p>
<span class="anchor" id="57c1c7d8-70c6-4adf-821b-92990f42b814"></span>
## 1.函数原型
<p>virtual int ReqQryProductGroup(CThostFtdcQryProductGroupField *pQryProductGroup, int nRequestID) = 0;</p>
<span class="anchor" id="3f2c4c13-ad94-4bd0-ac3c-f552d06f118d"></span>
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
<span class="anchor" id="f2368851-a0c5-4664-bd6b-5f79c2464be0"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="770b0b71-0220-4f7d-a416-32cc8dca3fc6"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="e442fb71-458b-4189-88ea-facef9d6f2fb"></span>
## 5.FAQ
<p>无</p>
