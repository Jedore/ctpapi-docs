<p>请求查询交易所</p>
<p>响应: <a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYEXCHANGE/">OnRspQryExchange</a></p>
<span class="anchor" id="8118507e-d2e2-4bdb-a3a9-99706a8c164a"></span>
## 1.函数原型
<p>virtual int ReqQryExchange(CThostFtdcQryExchangeField *pQryExchange, int nRequestID) = 0;</p>
<span class="anchor" id="f9050cf5-0b49-4073-8149-9bf1735afbac"></span>
## 2.参数
<p>pQryExchange：查询交易所</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcExchangeIDType</td>
<td style="TEXT-ALIGN: left;">ExchangeID</td>
<td style="TEXT-ALIGN: left;">交易所代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="a80488e8-38fc-455f-9266-2defec2d1d05"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="1a980a25-56d3-49c0-a0b2-af219c087fe4"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="22f35b95-61ed-4e14-a104-fe2f0132c9d0"></span>
## 5.FAQ
<p>无</p>
