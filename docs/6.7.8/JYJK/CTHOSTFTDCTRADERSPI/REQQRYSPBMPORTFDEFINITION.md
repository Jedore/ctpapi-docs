<p>请求SPBM组合保证金套餐查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYSPBMPORTFDEFINITION/">OnRspQrySPBMPortfDefinition</a></p>
<span class="anchor" id="3f16a08b-c9f9-4c10-99a8-b2a4b6d8af4c"></span>
## 1.函数原型
<p>virtual int ReqQrySPBMPortfDefinition(CThostFtdcQrySPBMPortfDefinitionField *pQrySPBMPortfDefinition, int nRequestID) = 0;</p>
<span class="anchor" id="cd756b9c-090d-4b95-98ca-4e354509251e"></span>
## 2.参数
<p>pQrySPBMPortfDefinition：组合保证金套餐查询</p>
<table><tr><th style="TEXT-ALIGN: center;">字段类型</th><th style="TEXT-ALIGN: center;">字段名称</th><th style="TEXT-ALIGN: center;">含义</th><th style="TEXT-ALIGN: center;">是否可作为过滤条件</th></tr><tr><td style="TEXT-ALIGN: left;">TThostFtdcExchangeIDType</td>
<td style="TEXT-ALIGN: left;">ExchangeID</td>
<td style="TEXT-ALIGN: left;">交易所代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcPortfolioDefIDType</td>
<td style="TEXT-ALIGN: left;">PortfolioDefID</td>
<td style="TEXT-ALIGN: left;">组合保证金套餐代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
<tr><td style="TEXT-ALIGN: left;">TThostFtdcInstrumentIDType</td>
<td style="TEXT-ALIGN: left;">ProdFamilyCode</td>
<td style="TEXT-ALIGN: left;">品种代码</td>
<td style="TEXT-ALIGN: left;"><strong><font color="#FF0000">是</font></strong></td>
</tr>
</table>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="f1d676c5-4506-43d4-bc72-0529984b2322"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="92213244-5266-454e-be44-3ed2b7364bd5"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="d235717e-cffa-4656-bf66-d49f8313f2eb"></span>
## 5.FAQ
<p>无</p>
