<p>请求SPBM期权合约参数查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYSPBMOPTIONPARAMETER/">OnRspQrySPBMOptionParameter</a></p>
<span class="anchor" id="860e6759-bfab-42ff-91e6-2335f4efa1e6"></span>
## 1.函数原型
<p>virtual int ReqQrySPBMOptionParameter(CThostFtdcQrySPBMOptionParameterField *pQrySPBMOptionParameter, int nRequestID) = 0;</p>
<span class="anchor" id="3412b52f-4272-47b8-9419-fcd6e03ad829"></span>
## 2.参数
<p>pQrySPBMOptionParameter：SPBM期权合约保证金参数查询</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcExchangeIDType</td>
<td style="TEXT-ALIGN: left;">ExchangeID</td>
<td style="TEXT-ALIGN: left;">交易所代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">InstrumentID</td>
<td style="TEXT-ALIGN: left;">合约代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">ProdFamilyCode</td>
<td style="TEXT-ALIGN: left;">品种代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="a2c0991e-3392-40d2-87d2-f82f145ef80b"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="aa78cdc2-b9b4-4185-88da-9ec255568336"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="a869ba92-2bfc-4d35-b1ba-2f52c87f8bfa"></span>
## 5.FAQ
<p>无</p>
