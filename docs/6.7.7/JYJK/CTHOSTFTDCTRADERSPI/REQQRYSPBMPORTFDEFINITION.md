<p>请求SPBM组合保证金套餐查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYSPBMPORTFDEFINITION/">OnRspQrySPBMPortfDefinition</a></p>
<span class="anchor" id="558a6459-7c1a-4373-983c-567b56714d5b"></span>
## 1.函数原型
<p>virtual int ReqQrySPBMPortfDefinition(CThostFtdcQrySPBMPortfDefinitionField *pQrySPBMPortfDefinition, int nRequestID) = 0;</p>
<span class="anchor" id="97e8fe5e-89a6-4725-a5ed-9fe8e6280635"></span>
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
<span class="anchor" id="cb43db6d-8259-4dec-b843-a37ffe5144b2"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="a0aa712a-1e68-49ba-9ac1-0da68d01356e"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="b6354c69-f4a6-481d-9062-982b60496aa4"></span>
## 5.FAQ
<p>无</p>
