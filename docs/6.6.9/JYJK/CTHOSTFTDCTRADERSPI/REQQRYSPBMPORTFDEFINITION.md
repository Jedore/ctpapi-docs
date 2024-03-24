<p>请求SPBM组合保证金套餐查询，对应响应请求<a href="../../CTHOSTFTDCTRADERAPI/ONRSPQRYSPBMPORTFDEFINITION/">OnRspQrySPBMPortfDefinition</a></p>
<span class="anchor" id="c23c18af-e318-4738-942c-d8ac57a2a329"></span>
## 1.函数原型
<p>virtual int ReqQrySPBMPortfDefinition(CThostFtdcQrySPBMPortfDefinitionField *pQrySPBMPortfDefinition, int nRequestID) = 0;</p>
<span class="anchor" id="a18938f6-bc5a-4eee-91e2-2f2a3019de05"></span>
## 2.参数
<p>pQrySPBMPortfDefinition：组合保证金套餐查询</p>
<pre><code>struct CThostFtdcQrySPBMPortfDefinitionField
{
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///组合保证金套餐代码
    TThostFtdcPortfolioDefIDType    PortfolioDefID;
    ///品种代码
    TThostFtdcInstrumentIDType  ProdFamilyCode;
};
</code></pre>
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
<span class="anchor" id="86fca7b6-eed4-4a75-a51c-fae124855e07"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="c7cc023a-ed77-4c17-9f2e-a0ac5edf60fd"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="0c84d53c-6e34-4373-92a4-f96f338f7815"></span>
## 5.FAQ
<p>无</p>
