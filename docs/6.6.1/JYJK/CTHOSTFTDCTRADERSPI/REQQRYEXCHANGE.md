<p>请求查询交易所</p>
<p>响应: <a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYEXCHANGE/">OnRspQryExchange</a></p>
<span class="anchor" id="be147c3f-fd55-4952-a4cb-a5e63face9d8"></span>
## 1.函数原型
<p>virtual int ReqQryExchange(CThostFtdcQryExchangeField *pQryExchange, int nRequestID) = 0;</p>
<span class="anchor" id="f876d8c0-0770-4d6b-9732-c0d6ffa107cd"></span>
## 2.参数
<p>pQryExchange：查询交易所</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcExchangeIDType</td>
<td style="TEXT-ALIGN: left;">ExchangeID</td>
<td style="TEXT-ALIGN: left;">交易所代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="465c31ff-07e0-44c6-8b5a-41ad75b56ced"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="d54929ca-a704-47b6-aa96-89c159688c60"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="17b5a7db-08e4-4fda-b950-431c28c49e55"></span>
## 5.FAQ
<p>无</p>
